# Survey to rate tweets

## Getting Started

Install the environment with conda and

```bash
$ conda env create
```

or follow the instructions on https://otree.readthedocs.io/en/latest/install.html to
install oTree.

## General Structure

This repo consists of several apps. There are apps for only one sentiment spanning ten
rounds, and integrated apps. The integrated apps are:

- <b> all_scales </b>
- <b> rate_tweets </b>

The first displays all possible rating scales to the participant, whereas the latter only displays one scale

### all_scales

This app runs 40 rounds and every round the participant can answer on all four scales. The tweets are distributed to the participants randomly.

### rate_tweets

This app runs 40 rounds and every 10 rounds it changes the choice of answer the
participant can give. The tweets are distributed to the participants randomly.

### Run the survey

To run the survey one has to navigate to the parent folder of the project. Then, run:

```bash
$ otree devserver
```

Follow the further instructions to get to the sessions.

## Resources

The documentation on https://otree.readthedocs.io/en/latest/ proved to be very useful in
programming the survey.
