from pydantic import BaseModel

# corpo da requisição para enviar mensagem (Q1).
class SendRequest(BaseModel):
    content: str

# estrutura de mensagem entregue (Q1).
class DeliverMessage(BaseModel):
    message_id: str
    sender_id: int
    timestamp: int
    content: str

# estrutura de ACK (Q1).
class AckMessage(BaseModel):
    message_id: str
    sender_id: int
    receiver_id: int

# configuração de atraso (para simular delay em mensagens).
class DelayConfig(BaseModel):
    message_id: str
    delay_ms: int
