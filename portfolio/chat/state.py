import os
import reflex as rx
from openai import OpenAI
import time

# Checking if the API key is set properly
if not os.getenv("OPENAI_API_KEY"):
    raise Exception("Please set OPENAI_API_KEY environment variable.")

# Ensure ASSISTANT_ID is set in the environment variables
if not os.getenv("ASSISTANT_ID"):
    raise Exception("Please set ASSISTANT_ID environment variable.")

class QA(rx.Base):
    """A question and answer pair."""

    question: str
    answer: str

DEFAULT_CHATS = {
    "Intros": [
        # TODO: Add some messages in here
    ],
}

class ChatState(rx.State):
    """The app state."""

    # A dict from the chat name to the list of questions and answers.
    chats: dict[str, list[QA]] = DEFAULT_CHATS

    # The current chat name.
    current_chat = "Intros"

    # The current question.
    question: str

    # Whether we are processing the question.
    processing: bool = False

    # The name of the new chat.
    new_chat_name: str = ""

    def create_chat(self):
        """Create a new chat."""
        # Add the new chat to the list of chats.
        self.current_chat = self.new_chat_name
        self.chats[self.new_chat_name] = []

    def delete_chat(self):
        """Delete the current chat."""
        del self.chats[self.current_chat]
        if len(self.chats) == 0:
            self.chats = DEFAULT_CHATS
        self.current_chat = list(self.chats.keys())[0]

    def set_chat(self, chat_name: str):
        """Set the name of the current chat.

        Args:
            chat_name: The name of the chat.
        """
        self.current_chat = chat_name

    @rx.var
    def chat_titles(self) -> list[str]:
        """Get the list of chat titles.

        Returns:
            The list of chat names.
        """
        return list(self.chats.keys())

    async def process_question(self, form_data: dict[str, str]):
        # Get the question from the form
        question = form_data["question"]

        # Check if the question is empty
        if question == "":
            return

        model = self.assistant_process_question

        async for value in model(question):
            yield value

    async def assistant_process_question(self, question: str):
        """Get the response from the Assistant API.

        Args:
            question: The current question.
        """

        # Add the question to the list of questions.
        qa = QA(question=question, answer="")
        self.chats[self.current_chat].append(qa)
        
        # Clear the input and start the processing.
        self.processing = True
        yield

        try:
            # Create a new Thread
            print("Creating thread")
            client = OpenAI()
            thread = client.beta.threads.create()
            print(f"Thread created: {thread.id}")

            # Add the question as a Message in the Thread
            print("Creating message")
            message = client.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=question
            )
            print(f"Message created: {message.id}")

            # Run the Assistant on the Thread
            print("Running assistant on thread")
            run = client.beta.threads.runs.create(
                thread_id=thread.id,
                assistant_id=os.getenv("ASSISTANT_ID")
            )
            print(f"Run created: {run.id}")

            # Wait for the run to complete
            print("Waiting for run to complete")
            while True:
                run_status = client.beta.threads.runs.retrieve(
                    thread_id=thread.id,
                    run_id=run.id
                )
                if run_status.status == "completed":
                    break
                time.sleep(1)  # Add a delay to avoid too frequent polling
            print("Run completed")

            # Retrieve the messages added by the Assistant to the Thread
            print("Retrieving messages")
            messages = client.beta.threads.messages.list(
                thread_id=thread.id
            )
            print(f"Messages retrieved: {len(messages.data)}")

            # Append the Assistant's response to the QA pair
            if messages and len(messages.data) > 1:
                for msg in messages.data:
                    if msg.role == "assistant":
                        self.chats[self.current_chat][-1].answer += msg.content[0].text.value
                        self.chats = self.chats
                        yield

        except Exception as e:
            print(f"Error: {e}")

        # Toggle the processing flag.
        self.processing = False