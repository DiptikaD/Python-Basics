We're hosting a party and we need to know how many hot dog buns we need and how many plant-based hot dogs.

Buns and dogs are sold in packs of different sizes:

    8 buns are in 1 pack of buns
    10 hot dogs are in 1 pack of dogs
Create a dog_and_bun_packs_needed function which accepts the number of guests and returns a two-item tuple containing the number of bun packs and the number of dog packs we need (bun packs first, dog packs second).

```python
dog_and_bun_packs_needed(7)
(1, 1)
dog_and_bun_packs_needed(10)
(2, 1)
dog_and_bun_packs_needed(14)
(2, 2)
dog_and_bun_packs_needed(20)
(3, 2)
dog_and_bun_packs_needed(21)
(3, 3)
dog_and_bun_packs_needed(28)
(4, 3)