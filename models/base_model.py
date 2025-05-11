#!/usr/bin/python3
"""This module contains the BaseModel class."""

import uuid
from datetime import datetime

class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ("created_at", "updated_at"):
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates `updated_at` with current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns dictionary representation of the instance."""
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result

