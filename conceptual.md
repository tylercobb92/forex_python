### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript? 
	- Javascript is primarily used for front end work while Python is used for back end work.  
	- Javascript runs on the client side, while Python runs on a server.       

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you can try to get a missing key (like "c") *without* your programming crashing.  
	- One way is to use get(), which will return the value of the key entered or the second argument as the default if no matching key exists:  
		>In: dictionary.get('a','key not found')  
		>Out: 1  
		>In: dictionary.get('c','key not found')  
		>Out: 'key not found'

	- Another way is to use setdefault(), which works similar to get() but adds the missing key and the default value to the dictionary:  
		>In: dictionary.setdefault('a','key not found')  
		>Out: 1  
		>In: dictionary.setdefault('c','key not found')
		>Out: 'key not found'  
		>In: dictionary  
		>Out: {'a': 1, 'b': 2, 'c': 'key not found'}

- What is a unit test?  
	- A unit test tests individual components within a Python application. 

- What is an integration test?
	- Integration tests check that components within an application work together, not just as separate functions.

- What is the role of web application framework, like Flask?
	- The role of web application frameworks is to allow development of applications by compiling different libraries to handle tasks instead of writing new code for everything.

- You can pass information to Flask either as a parameter in a route URL (like '/foods/pretzel') or using a URL query param (like 'foods?type=pretzel'). How might you choose which one is a better fit for an application?
	- Using a URL route would be better for broad categories, such as defining a landing/home page or a page with a form. For instance a page /dog/breeds which contains a list of breeds. 
	- Using a query parameter would be better for specific details, such as a search that could include multiple values like /dog/breeds?hypoallergenic=yes&color=brindle which narrows the search by two separate parameters.

- How do you collect data from a URL placeholder parameter using Flask?
	- Placeholders data can be collected using literal strings
	>@app.route('dog/breeds/<breed>')  
	>>def get_breed:  
	>>>return f'Breed is {breed}' 

- How do you collect data from the query string using Flask?
	- This can be done using request. To return the color parameter from the above example which searched for breeds of dog that are both hypoallergenic and brindle:
	>@app.route('/dog/breeds')
	>>def get_color():
	>>>return request.args.get('color')

- How do you collect data from the body of the request using Flask?
	- This can also be done using request and specifying request.form, request.data, or request.json, as well as methods=['POST']. In the case of data entered into a form specifying a breed of dog to search:
	>@app.route('/dog/breeds', methods=['POST'])
	>>def get_breed():
	>>>data=request.form  
	>>>return data['breed']

- What is a cookie and what kinds of things are they commonly used for?
	- Cookies are bits of data that store information such as remembered usernames, passwords, and pages/links that have already been visited. All of this information is used to identify users and remember their site preferences.

- What is the session object in Flask?
	- The session object tracks information specific to a session of web browsing. This information is not remembered when the page is closed, unlike cookies. 

- What does Flask's `jsonify()` do?
	- jsonify() turns data into json data, which is made up of key:value pairs and can be read by multiple languages. This is useful for communication between back end and front end.  
