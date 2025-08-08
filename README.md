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


## Images

"beatingfloatspaper.png" [1]
"Atari_1040STf_v2.jpg" [3]


## References

[1] Gustafson, J. L., & Yonemoto, I. T. (2017). Beating Floating Point at its Own Game: Posit Arithmetic. *Supercomputing Frontiers and Innovations*, 4(2), 71–86. https://doi.org/10.14529/jsfi170206  

[2] Y. Uguen, L. Forget and F. de Dinechin, "Evaluating the Hardware Cost of the Posit Number System," *2019 29th International Conference on Field Programmable Logic and Applications (FPL)*, Barcelona, Spain, 2019, pp. 106-113, doi: 10.1109/FPL.2019.00026. keywords: {Standards;Hardware;Encoding;Libraries;Decoding;Open source software;Computer architecture;posit;architecture;fpga}  

[3] Bill Bertram (2006), Atari 1040STf (1986), Own work, CC BY-SA 2.5, via Wikimedia Commons. https://de.wikipedia.org/wiki/Datei:Atari_1040STf.jpg  


## License

See [MIT License](https://github.com/kadsendino/some4?tab=MIT-1-ov-file).
