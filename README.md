# Some4

Animations for Some4

## Installation

You have to install `python-uv` and `git`

Clone repository and install manim:

```
git clone https://github.com/kadsendino/some4.git
cd some4
uv add manim
```

Run manim example scene `CreateCircle` from `main.py`:

```
uv run manim -pql main.py CreateCircle
```

## Voiceover

For using voiceover run:

```
uv add gtts
uv run gtts voiceover_test.py
```

For add it to animation:

```
uv add pydub
uv run manim -pql voiceover_specialcases.py SpecialCases
```

## Contribution

To create scenes please use the `main` branch but different files than `main.py`. In the end the finished scenes will be combined in `main.py`.

## Documentation

For documentation please visit the [Manim Community Website](https://docs.manim.community).

## License

See [MIT License](https://github.com/kadsendino/some4?tab=MIT-1-ov-file).
