# Platform Technical Screen

# robotic-automation-factory

---

created: 2024-12-31T20:18:33 (UTC -05:00)
source: <https://thoughtfulautomation.notion.site/Platform-Technical-Screen-b61b6f6980714c198dc49b91dd23d695>
author: Mr. Gal Levinshtein
---

## Project Setup and Run Instructions

### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

### Setup Steps

1. Clone the repository:

```bash
git clone https://github.com/your-repo/robotic-automation-factory.git
cd robotic-automation-factory
```

2. Create a virtual environment and activate it:

# On Windows

```
python -m venv venv
venv\Scripts\activate
```

# On macOS/Linux

```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Run the test coverage script:
```
pytest
```

---

# Platform Technical Screen

![](https://thoughtfulautomation.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F1eec7df9-d484-4330-b2c6-8078b2cdeb0e%2F65e82bd0-dfac-457f-af29-3727fce75c5e%2FUntitled.png?table=block&id=7541fdf1-c832-4358-b64b-6996e182f3de&spaceId=1eec7df9-d484-4330-b2c6-8078b2cdeb0e&width=1420&userId=&cache=v2)


#### Objective

Imagine you work in Thoughtful’s robotic automation factory, and your objective is to write a function for one of its robotic arms that will dispatch the packages to the correct stack according to their volume and mass.

#### Rules

Sort the packages using the following criteria:

A package is bulky if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.

A package is heavy when its mass is greater or equal to 20 kg.

You must dispatch the packages in the following stacks:

STANDARD: standard packages (those that are not bulky or heavy) can be handled normally.

SPECIAL: packages that are either heavy or bulky can't be handled automatically.

REJECTED: packages that are both heavy and bulky are rejected.

#### Implementation

Implement the function sort(width, height, length, mass) (units are centimeters for the dimensions and kilogram for the mass). This function must return a string: the name of the stack where the package should go.

#### Submission Guidance

1. Time Management: Allocate no more than 30 minutes to complete this challenge.

2. Programming Language: You may use any programming language you're comfortable with. This is an opportunity to showcase your skills in a language you are proficient in.

2. Submission Format:

- Option 1: Submit a public GitHub repository with clear README instructions.

- Option 2 (Preferred): Host your solution on an online IDE like [Repl.it](http://repl.it/) or CodePen for immediate code review. Ensure the link is accessible for direct execution.

3. Evaluation Criteria: Submissions will be assessed on:

- Correct sorting logic.

- Code quality.

- Handling edge cases and inputs.

- Test coverage.


