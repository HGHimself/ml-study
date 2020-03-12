# Bayes Theorem

The example problem here is "salmon vs seabass". If you were to pull a fish out of the ocean, what are the odds that it is a salmon versus a seabass? 
This is a perfect example of a classification problem. As with any classification problem, there are some questions that need answers. Lets take a look:
- What features are we going to look at?
- Which of these features are the best?
- How do we separate out classes?
- How can we tell if we are classifying correctly?

## Classifiers

You can imagine a given fish that has various features and traits. you can take the length of the fish and use that to try and guess. 
But there is probably a higher margin of error than if you were to use length and color. Now that you have two dimensions of classification,
you can begin to map the cutoff line between these two data clusters. The key here is know how to draw this line. Sometimes you can be too niave,
too specific, or just right.

How are we able to do something like this?

e.x.
Image you have four boxes. 
1. 2000 components, 100 defective
2. 400 components, 160 defective
3. 1000 components, 100 defective
4. 1000 components, 100 defective

What is the probability of getting a defetive component?

let B_j be the event "pick box j"
let d be the event "pick a defective component"

Bayes Formula states teh following:

P(B_j | D) = P(D | B_j) * P(D) / P(B_j)

