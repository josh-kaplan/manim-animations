# Manim Animations

To build a scene run `make path/to/scene` where the path starts from the
`src/scenes` directory. For example, to build the `MovingAngle` scene, run
`make 00-scratchpath/MovingAngle`.


**Building with Manim directly**

To make:
manim -p -ql moving-angle.py MovingAngle


For higher quality:
manim -p -gh MovingAngle


## Code Structure

- `src/scenes` - These are individual manim scenes organized roughly by topic.
    - `00-scratchpad` - This section is for exploring tutorials and manim concepts.
- `src/util` - Reusable utility classes and functions.
