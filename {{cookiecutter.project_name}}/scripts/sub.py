import re
import unittest
from pathlib import Path
from pprint import pprint

root_dir = Path(__file__).parent.parent
src_dirs = [
    root_dir.joinpath("src"),
    root_dir.joinpath("tests"),
    root_dir.joinpath("config"),
]
dst_root = root_dir.joinpath("dist")
dst_root.mkdir(parents=True, exist_ok=True)
project_name = "my-client-project"
project_slug = project_name.replace("-", "_")
patterns = {
    re.compile(project_slug): "{{cookiecutter.project_slug}}",
    re.compile(project_name): "{{cookiecutter.project_name}}",
}
file_pattern = re.compile(".*\.(py|toml|md|yaml)$")


def main():
    q = [*src_dirs]

    while q:
        item = q.pop(0)
        dst_item = dst_root.joinpath(item.relative_to(root_dir))
        if item.is_dir():
            dst_item.mkdir(parents=True, exist_ok=True)
            for sub_item in item.iterdir():
                q.append(sub_item)
            continue
        elif item.is_file() and file_pattern.match(item.name):
            with open(item, "r", encoding="utf-8") as read_stream:
                lines = read_stream.readlines()
            # 文本替换
            sublines = replace_lines(lines, patterns)
            with open(dst_item, "w", encoding="utf-8") as write_stream:
                write_stream.writelines(sublines)


def replace_lines(lines: list[str], patterns: dict[re.Pattern, str]) -> list[str]:
    res = []
    for line in lines:
        subline = line
        for _pat, _sub in patterns.items():
            subline = _pat.sub(_sub, subline)
        res.append(subline)
    return res


class TestCase(unittest.TestCase):

    def test_replace_lines(self):
        res = replace_lines(
            [f"hello, {project_slug}", f"world, {project_name}"], patterns
        )
        pprint(res)

    def test_sub(self):
        main()


if __name__ == "__main__":
    unittest.main()
