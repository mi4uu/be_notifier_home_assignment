from typing import Optional, Union
from be_notifier.entities import Entity
from be_notifier.rules import RULES


def notify(
    new: Optional[Entity] = None, old: Optional[Entity] = None
) -> Union[Entity, None, bool]:
    #
    # take new and old entity (or None)
    # return entity to notify or False if no notification is needed
    #
    if new is None and old is None:
        raise Exception("Both entities are None")

    # we could check in runtime if the entities are of compatible type
    # but it depends on the use case

    if new is not None and old is not None and type(new) is not type(old):
        raise Exception("Entities are not of the same type")

    obj_type: Entity = new.__class__ if new is not None else old.__class__  # type: ignore
    rules = RULES[obj_type]["rules"]
    target = RULES[obj_type]["target"]
    for rule in rules:
        if rule(new, old):
            return target(new, old)
    return False
