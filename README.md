# Survey to rate tweets

![](https://media.giphy.com/media/l4Xicqrij80QCgozCW/giphy.gif)

## Getting Started

Install the environment with conda and

```bash
$ conda env create
```

or follow the instructions on https://otree.readthedocs.io/en/latest/install.html to
install oTree.

## General Structure

This repo consists of several apps, the furthest developed is called two_scales. It displays two scales for 50 tweets.


To run the surveys one has to navigate to the parent folder of the project. Then, run:

```bash
$ otree devserver
```

Follow the further instructions to get to the sessions.

### bots

The apps have bots configured who randomly choose their answers.
Run them from the command line with:

```bash
$ otree test two_scales
```

When you are interested in the produced data, use:

```bash
$ otree test two_scales --export=out_data
```

## Resources

The documentation on https://otree.readthedocs.io/en/latest/ proved to be very useful in
programming the survey.
