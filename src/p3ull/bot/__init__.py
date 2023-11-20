import importlib
import logging
import os
import pkgutil
import typing as t

import disnake
from disnake.ext import commands
from disnake.ext.commands import AutoShardedInteractionBot

intents = disnake.Intents.all()

def walk_modules(
    paths: t.Iterable[str],
    prefix: str = "",
    ignore: t.Iterable[str] = None
) -> t.Iterator[str]:

    if isinstance(ignore, t.Iterable):
        ignore_tup = tuple(ignore)
        def ignore(path): return path.startswith(ignore_tup)

    seen: set[str] = set()

    for _, name, ispkg in pkgutil.iter_modules(paths, prefix):
        if ignore is not None and ignore(name):
            continue

        if not ispkg:
            yield name
            continue

        module = importlib.import_module(name)

        if hasattr(module, "setup"):
            yield name
            continue

        sub_paths: list[str] = []

        for path in module.__path__ or ():
            if path not in seen:
                seen.add(path)
                sub_paths.append(path)

        if sub_paths:
            yield from walk_modules(sub_paths, name + ".", ignore)


class Playa3ull(AutoShardedInteractionBot):
    def __init__(self):

        super().__init__(owner_id=485183782328991745, intents=intents, activity=disnake.Activity(type=disnake.ActivityType.watching, name="w3ull"))

    def _load_extensions(
        self,
        root_module: str,
        *,
        package: str = None,
        ignore: t.Iterable[str] = None,
    ) -> None:
        if "/" in root_module or "\\" in root_module:
            path = os.path.relpath(root_module)
            if ".." in path:
                raise ValueError(
                    "Paths outside the cwd are not supported. Try using the module name instead."
                )
            root_module = path.replace(os.sep, ".")

        root_module = self._resolve_name(root_module, package)

        if (spec := importlib.util.find_spec(root_module)) is None:
            raise commands.ExtensionError(
                f"Unable to find root module '{root_module}'", name=root_module
            )

        if (paths := spec.submodule_search_locations) is None:
            raise commands.ExtensionError(
                f"Module '{root_module}' is not a package", name=root_module
            )
        for module_name in walk_modules(paths, f"{spec.name}.", ignore):
            self.load_extension(module_name)
            logging.info(f"loaded {module_name}")
