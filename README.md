# twitch_test
test-task for twitch
_______________________________________________________________________________________________________________________
To run the tests, you need to run the command in the terminal:
pytest -q --tb=short

My example of run and result:
PS C:\Users\Admin\IdeaProjects\twitch_test\.idea> pytest -q --tb=short
DevTools listening on ws://127.0.0.1:62732/devtools/browser/6a6c71ba-c9a1-4233-b986-7815c7df9121
. [100%]
1 passed in 18.70s
________________________________________________________________________________________________________________________
Project Structure
The project is organized into several directories and files, which are structured as follows:

twitch_tests/.idea/
│

├── tests/

│   ├── __init__.py

│   ├── test_twitch.py

│

├── page_objects/

│   ├── __init__.py

│   ├── twitch_page.py

│   ├── twitch_locators.py

│

├── utils/

│   ├── __init__.py

│   ├── webdriver_manager.py

│

└── requirements.txt


Explanation of the Structure:
1. Root Directory (twitch_tests/):
This is the main directory that contains all the project files and directories. Keeping everything organized under a single root folder makes it easy to manage and navigate the project.
2. Tests Directory (tests/):
This directory contains the test files. 
__init__.py: This file indicates that the directory should be treated as a Python package, allowing imports across the package.
test_twitch.py: This file contains the actual test cases. By having a dedicated file for tests, it keeps the testing logic separate from the application logic, making the code cleaner and easier to maintain.
3. Page Objects Directory (page_objects/):
This directory implements the Page Object Model (POM) design pattern, which helps in organizing code related to the UI elements and actions of the application being tested.
__init__.py: Similar to the tests directory, it marks this directory as a package.
twitch_page.py: This file defines the TwitchPage class, which contains methods to interact with the Twitch website. This encapsulation allows for better code reusability and maintainability.
twitch_locators.py: This file contains element locators used in the TwitchPage class, centralizing the management of locators and making it easier to update them if the UI changes.
4. Utils Directory (utils/):
This directory contains utility functions and classes that support the main testing logic.
__init__.py: Again, this file indicates that the directory is a package.
webdriver_manager.py: This file includes the WebDriverManager class, which manages the setup and configuration of the Selenium WebDriver. By separating this into a utility, it promotes cleaner code and makes the WebDriver configuration reusable across different test cases.
5. Requirements File (requirements.txt):
This file lists all the dependencies needed for the project, such as Selenium and pytest. It allows for easy installation of all required libraries using a package manager like pip, ensuring that the environment is set up correctly for running the tests.

Why This Structure?
- Separation of Concerns: Each directory and file has a specific role, making the codebase easier to understand and maintain. Tests are separated from the application logic and UI interactions.
- Reusability: By following the Page Object Model, the project encourages reusability of code. The methods defined in the page object classes can be reused across multiple tests, reducing code duplication.
- Scalability: This structure is scalable, allowing for the addition of more tests or page objects as the project grows without becoming disorganized.
- Maintainability: By organizing the project in a logical manner, it becomes easier to make updates and modifications. If a UI element changes, you only need to update the locator in one place.
- Collaboration: A well-structured project makes it easier for multiple developers to collaborate, as they can quickly understand the layout and find the files they need to work with.
Overall, this project structure enhances clarity, organization, and efficiency in the development and testing process.
