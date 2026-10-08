from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base


class Applicant(Base):
    __tablename__ = "applicants"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=True)
    phone = Column(String(50), nullable=True)
    country = Column(String(100), nullable=True)

    education = Column(String(500), nullable=True)
    degree = Column(String(300), nullable=True)
    field = Column(String(300), nullable=True)

    experience = Column(Text, nullable=True)

    target = Column(String(300), nullable=True)
    german_level = Column(String(50), nullable=True)
    english_level = Column(String(50), nullable=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    documents = relationship(
        "Document",
        back_populates="applicant",
        cascade="all, delete-orphan"
    )

    agent_executions = relationship(
        "AgentExecution",
        back_populates="applicant",
        cascade="all, delete-orphan"
    )


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    applicant_id = Column(
        Integer,
        ForeignKey("applicants.id"),
        nullable=True
    )

    filename = Column(String(300), nullable=False)
    file_path = Column(String(500), nullable=True)
    document_type = Column(String(100), nullable=True)

    extracted_text = Column(Text, nullable=True)

    verification_status = Column(
        String(100),
        nullable=True
    )

    verification_confidence = Column(
        String(50),
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    applicant = relationship(
        "Applicant",
        back_populates="documents"
    )


class AgentExecution(Base):
    __tablename__ = "agent_executions"

    id = Column(Integer, primary_key=True, index=True)

    applicant_id = Column(
        Integer,
        ForeignKey("applicants.id"),
        nullable=True
    )

    action = Column(
        String(200),
        nullable=False
    )

    status = Column(
        String(100),
        nullable=True
    )

    reasoning = Column(
        Text,
        nullable=True
    )

    result = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    applicant = relationship(
        "Applicant",
        back_populates="agent_executions"
    )