# Sothebys


Sothebys is a marketplace for art. 

# Models

  - Buyer- first name, last name, email, password, phone, shipping
  - Seller- first name, last name, email, password, phone, description, logo
  - Artist- name, image, nationality, description, date of birth, date of death
  - Paintings- title, image, description, medium, price, artist (Foreign Key)
  - Order- timestamp, item (Foreign Key- painting), buyer (Foreign Key), seller (Foreign Key)
  - Review- text, order_id (Foreign Key- order)



### API's

We currently have the APIs listed below for Buyers, Sellers, Artists and Paintings.

#### Buyer API's


| API | REQUEST | FUNCTION | COMMENTS |
| ------ | ------ | ----- | ----- |
| /api/v1/buyers/ | GET | Get all Buyers | NA
| /api/v1/buyers/id/ | GET | Get the buyer with specified id | NA
| /api/v1/buyers/id/ | POST | Update a Buyer | Post data as form data (key, value pairs) with only the keys that you want to update


#### Seller API's


| API | REQUEST | FUNCTION | COMMENTS |
| ------ | ------ | ----- | ----- |
| /api/v1/sellers/ | GET | Get all Sellers | NA
| /api/v1/sellers/id/ | GET | Get the seller with specified id | NA
| /api/v1/sellers/id/ | POST | Update a Seller | Post data as form data (key, value pairs) with only the keys that you want to update

#### Painting API's


| API | REQUEST | FUNCTION | COMMENTS |
| ------ | ------ | ----- | ----- |
| api/v1/paintings/ | GET | Get all Paintings | NA
| api/v1/paintings/<int:id>/ | GET | Get the painting with specified id | NA
| api/v1/paintings/create/ | POST | Create a painting | Post data as form data (key, value pairs) with all the fields in Painting Model
| api/v1/paintings/<int:id>/update/ | POST | Update the painting with specified id | Post data as form data (key, value pairs) with only the keys that you want to update
| api/v1/paintings/<int:id>/delete/ | POST | Delete a painting by id| 


#### Artist API's


| API | REQUEST | FUNCTION | COMMENTS |
| ------ | ------ | ----- | ----- |
| api/v1/artists/ | GET | Get all Artists | NA
| api/v1/artists/<int:id>/ | GET | Get the artist with specified id | NA
| api/v1/artists/create/ | POST | Create an artist | Post data as form data (key, value pairs) with all the fields in Artist Model
| api/v1/artists/<int:id>/update/ | POST | Update the artist with specified id | Post data as form data (key, value pairs) with only the keys that you want to update
| api/v1/artists/<int:id>/delete/ | POST | Delete an artist by id| 

### Starting the Django App and the MySQL DB Container
To start the service, type the following command in the root directory of the project.
```sh
$ docker-compose up
```

# User Stories
- As a prospective buyer I want to be able to learn more about a painting I like.
	
- As a prospective buyer I want to see all the paintings of the artist whose painting/work I'm interested in.
	
- As a user I want to be able to view the most recently added works.
	
- As a seller I want to specify and display the price of my products.
	
- As a user I want to have the information about the marketplace available to me so that I know where I am shopping. 
	
- As a buyer I want to be able to read more about the artist of a work I'm interested in so that I can better understand the work.
  
- As a user I want to be able to be able to register an account on the website

- As a user I want to be able to log in to Sothebeys

- As a seller I want to be able to create new listings for my products on the website

