#!/usr/bin/python3
"""

"""

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary


if __name__ == "__main__":
    my_model = BaseModel()
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    for key in my_model_json:
        print(
            "\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key])
        )

    # Creating an instance with kwargs
    kwargs = {
        "id": "123",
        "created_at": "2023-06-06T12:00:00.000000",
        "updated_at": "2023-06-06T12:00:00.000000",
        "name": "Test Model"
    }
    my_model_from_kwargs = BaseModel(**kwargs)
    print(my_model_from_kwargs)
    my_model_from_kwargs_json = my_model_from_kwargs.to_dict()
    print(my_model_from_kwargs_json)
    for key in my_model_from_kwargs_json:
        print(
            "\t{}: ({}) - {}".format(key, type(my_model_from_kwargs_json[key]), my_model_from_kwargs_json[key])
        )

