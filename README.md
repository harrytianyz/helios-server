# Carleton Helios

This is part of the Voting machine comps of the 2020-21 Carleton CS comps. 

Advisor: Sneha Narayan 

Members: Harry, James, John, Judy, Kate, Matthew

This project is based off of [Helios Voting](https://vote.heliosvoting.org/), a web-based open-audit electronic voting system. In our implementation, we added modular security features that allow administrators to customize the election's degree of verifiability

## Implementation

A key feature of Helios is its open-audit, ["true-verifiable"](https://vote.heliosvoting.org/faq) nature. That is, anyone can verify *anyone's* votes *at any time*. We implemented a customizable version of this where the when creating an election, the adminstrator can modify the following options, where the options are in brackets:

When the election is open: 
* non-administrators can audit votes belonging to **\[anyone, themselves, nobody\]**
* administrators **\[can, cannot\]** audit votes.

When the election is closed: 
* non-administrators can audit votes belonging to **\[anyone, themselves, nobody\]**
* administrators **\[can, cannot\]** audit votes.

## Code changes

We added Django fields to the forms and models by modifying `helios/models.py`,  `helios/views.py`, `helios/forms.py`, `helios/migrattions/0001_initial.py`, although it is unsure if all of those changes are necessary.

To the implement the verifiability options, we enabled or disabled access to voters' encrypted ballot, which can be used to verify votes. Changes were made to `templates/voters_list.html` and `templates/castvote.html`. Unit tests were checked for the changes to templates/voters_list.html but not for templates/castvote.html.
