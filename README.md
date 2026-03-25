# Currency Converter

![image](https://github.com/user-attachments/assets/f1db2799-e4a3-4eb4-9aea-d1556038d3ea)

A simple graphical application for currency conversion, developed in Python using [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for a modern and stylish interface.

## Features

- Conversion between various international currencies.

- User-friendly and responsive interface.

- Display of the conversion rate used.

- Rounded corners in the input and selection boxes.

![image](https://github.com/user-attachments/assets/050a8226-a3ca-4a7b-9575-08431910f6d6)

## How to use

1. **Clone the repository** and access the project folder.

2. **Install the dependencies**:

```
pip install -r requirements.txt

```
3. **Run the application**:

```
python app.py

```

## API key configuration

Create a `.env` file in the project root with the following content:

``` API_KEY=your_key_here

```

Replace `your_key_here` with your Free Currency API key. To generate a key, you need to register on the API website.

## API Used

- [Free Currency API](https://freecurrencyapi.com/)

The Free Currency API was used to obtain real-time exchange rates between the selected currencies. The project makes an HTTP request to the API whenever the user requests a conversion, ensuring that the values ​​are always up-to-date. Using the API provided practical learning on how to consume external services in Python, handle HTTP requests, process JSON responses, and manage potential connection or data errors.

## Graphical Interface

The interface was built with CustomTkinter, a modern extension of Tkinter that allows for the creation of more beautiful and customizable visual components, such as input boxes and buttons with rounded corners and custom colors. Developing the graphical interface provided experience with absolute and relative widget positioning, event handling (such as button clicks), window centering, and applying styles to improve the user experience.

## Video used as a basis

- [YouTube: Currency Converter (in English)](https://youtu.be/zT7niRUOs9o?si=7joc0xuNQ4b_BPH9)

---

## Lessons Learned

By carrying out this project, it was possible to deepen knowledge in:

- Consuming REST APIs in Python.

- Manipulating JSON data.

- Handling exceptions and error messages for the user.

- Creating modern and responsive graphical interfaces with CustomTkinter.

- Organizing code into reusable functions and separating responsibilities.

- Improving the user experience with visual feedback and window centering.

This project is a great foundation for those who want to learn integration between Python, external APIs, and graphical interfaces, as well as good usability practices.
