# Meetup Redesign Tracking

## Current State
- Phase 1: Creative Burst (Fan-Out) started.
- Goal: Redesign OpenClaw Prague Meetup landing page with smaller sections and specific SVGs. Date updated to March 26, 2026.
- Knowledge: `index.html` read.

## Delegation Log
*No delegations yet.*

## Reasoning Log
*No decisions made yet.*

## Iterative Visual Refinements (Playwright Directed)

- **Iteration 1**: Upgraded the `<details>`/`<summary>` dropdown styling with full transitions, +/- toggles, and better grouping.
- **Iteration 2**: Introduced glassmorphism (`backdrop-filter: blur()`) to `.section` and hover translation `translateY` for an elevated card feel.
- **Iteration 3**: Styled the `.bio-photo` class with glowing box shadows, 1.08 scale scaling, and slight rotation (+`5deg`) upon hover.
- **Iteration 4**: Typography boost on the hero unit! Added a horizontally looping gradient shift (`animation: gradient-shift 3s linear infinite`) to the `h1` component and added tracking (`letter-spacing`) to the tagline.
- **Iteration 5**: Elevated `.btn` elements by increasing padding, font-weight, adding letter-spacing (uppercase), box-shadow initialization state, and transforming `-3px` upwards on hover.

Page is looking vibrant, sleek, and animated.

## User Requests & Iterations
- "Make it breathe more": Increased section margins to `100px 0` and padding to `50px`.
- "What to expect": Added a clear 17:30 - Midnight agenda for open talk, demo shows, and hacker hours.
- Removed "What is OpenClaw" so people without experience don't apply, ensuring better attendee signaling.
- Rewrote the Registration text pushing applicants to provide 2 sentences about themselves and their tinkering. 
- Removed the abstract background styling and confusing SVG from the Community block. 
- Enhanced the hero section by adding a glowing floating date badge pinned at the top.

## Content Extraction
- Moved all textual copy out into a separate `content.js` file for easy updating.
- The `index.html` has been refactored to pull DOM strings from the `.js` file via standard native injection (No framework needed).

## Iteration: Mascot Fix & Luma Asset Generator
- **User Feedback**: The skyline graphic was terrible, not quirky. And the mascot had 3 legs instead of 4.
- **Fixes**: Replaced the mascot SVG `<path>` definition across `index.html`, `openclaw-mascot-static.svg`, and `openclaw-luma-square.svg` to feature 4 evenly spaced legs.
- **Visual Variations**: In response to the request for 10 quirky, simple Prague-vibes iterations, wrote a Python + `cairosvg` script to generate 10 unique compositions (e.g., Beer Bath, Tram 22, Defenestration, Red Roofs, Golem, Trdelnik) into `tmp/iterations/`.
- **Status**: Variations generated and opened in Finder.

## Iteration: Trdelnik Mascot Icons
- **User Feedback**: Iterate 10x on the "Trdelnik Cat" idea specifically, optimizing for extreme clarity at tiny sizes.
- **Fixes**: Removed thin lines and tiny typography from the templates. Scaled the mascot geometry by 10x to 20x relative to the canvas.
- **Visual Variations**: Created 10 compositions entirely dedicated to the Trdelnik theme (e.g. Stacked Rings, Diagonal Wrap, Donut Hole, Trdelnik Crown, Mega Bite).
- **Status**: SVGs and PNGs generated in `tmp/trdelnik_iterations/` and opened for review.
