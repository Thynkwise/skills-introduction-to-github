class OutboundAgent:
    """Simple AI-based outbound agent using sentiment keywords."""

    POSITIVE_WORDS = {
        'yes', 'sure', 'interested', 'okay', 'ok', 'great', 'sounds', 'good',
        'love', 'like'
    }
    NEGATIVE_WORDS = {
        'no', 'not', "don't", 'stop', 'never', 'hate', 'bad'
    }

    def __init__(self):
        self.positive_script = [
            "Hello! I'd love to tell you about our new product.",
            "Great! Let me share more details with you.",
            "Thanks for your interest. I'll send more info shortly."
        ]
        self.negative_script = [
            "I'm sorry to bother you. Have a nice day!",
            "Understood. I'll remove you from our list.",
            "Thank you for your time. Goodbye."
        ]
        self.pos_idx = 0
        self.neg_idx = 0

    def _analyze_sentiment(self, text: str) -> str:
        words = text.lower().split()
        score = sum(w in self.POSITIVE_WORDS for w in words)
        score -= sum(w in self.NEGATIVE_WORDS for w in words)
        return 'positive' if score >= 0 else 'negative'

    def respond(self, customer_response: str) -> str:
        sentiment = self._analyze_sentiment(customer_response)
        if sentiment == 'positive':
            if self.pos_idx < len(self.positive_script):
                msg = self.positive_script[self.pos_idx]
                self.pos_idx += 1
            else:
                msg = "Thank you for your continued interest!"
        else:
            if self.neg_idx < len(self.negative_script):
                msg = self.negative_script[self.neg_idx]
                self.neg_idx += 1
            else:
                msg = "Apologies for the inconvenience. Goodbye."
        return msg

