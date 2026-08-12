class VoiceAssistantEngine:
    def __init__(self):
        self.commands = {
            "open dashboard": "Launching SaaS Analytics Dashboard...",
            "run security scan": "Executing AI Red-Teaming simulation...",
            "generate dataset": "Generating synthetic privacy-preserving dataset...",
            "summarize codebase": "Analyzing repository and generating summary..."
        }

    def process_voice_command(self, transcript: str):
        transcript_lower = transcript.lower()
        for cmd, action in self.commands.items():
            if cmd in transcript_lower:
                return {"status": "success", "command": cmd, "response": action}
        return {"status": "unknown", "command": transcript, "response": "Command not recognized. Try 'open dashboard' or 'run security scan'."}
