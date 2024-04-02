# Shot Noise RNG

Implementation of a PRNG in python using Shot Noise as a random source. I'm implementing PRNG such as Fortuna, Yarrow and Blum Blum Shub.

For the noise generator, I'm using the camera of my laptop.

# 🚧 Work in progress 
## TODO
- Fortuna, Generator and Accumulator classes
- iterate_counter() algorithm
- create a flag so the rng can stop to a given time

## Done:
- camera byte stream for rng source

## Later:
- Yarrow PRNG
- Blum Blum Shub
- Maybe other RNG sources

# Installation

Should work for every python3 version.
Launch this command:
```bash
pip3 install -r requirements.txt
```

Then you can use the Fortuna PRNG from [main.py](main.py).

# 🔗 Sources:

- [Cryptography Engineering Design Principles and Practical Applications](https://www.schneier.com/wp-content/uploads/2015/12/fortuna.pdf)
- [Wikipedia - Poisson_distribution](https://en.wikipedia.org/wiki/Poisson_distribution)
- [SERIOUS CRYPTOGRAPHY: a Practical Introduction to Modern Encryption by Jean-Philippe Aumasson](https://palaiologos.rocks/library/Serious%20Cryptography%20Jean-Philippe%20Aumasson.pdf)