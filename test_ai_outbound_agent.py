from ai_outbound_agent import OutboundAgent


def test_positive_response():
    agent = OutboundAgent()
    message = agent.respond("Yes, I'd like more information")
    assert "Hello" in message or "Great" in message


def test_negative_response():
    agent = OutboundAgent()
    message = agent.respond("No thanks, stop calling")
    assert "sorry" in message.lower() or "understood" in message.lower()
