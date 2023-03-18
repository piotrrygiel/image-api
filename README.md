# image-api
API that allows authenticated user to upload images. We can create account tiers and attach them to users so they have different privileges. User get a paginated list of links to uploaded images and/or thumbnails.

## Project set up
Follow the steps below to get started with this project's development environment.
> _Note_: You need docker installed on your PC to run the project.
1. Download repository and extract files.
2. Open terminal/CMD and navigate to project root folder (where docker-compose.yml is located).
3. Write command:
```sh
docker-compose up
```
and wait for container to be prepared.
> _Note_: I noticed that the first time you run `docker-compose up` command you may have to wait until all instructions are executed and then press `Ctrl + C` to exit the process.
4. Now you can write command:
```sh
docker-compose up
```
again and image should be up and running.
5. We have to create Django superuser now. Open second terminal window, navigate to project root folder and run command:
```sh
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```
provide username and password (email can be ommited).

## Further configuration
1. You can now login to admin panel with your credentials. Go to localhost (`http://127.0.0.1:8000/admin`) and login with your superuser account.
2. We can now create "builtin" account tiers as well as custom tiers.
3. We can also create users and assign them tier.
4. When we have created tiers and users we can go to `http://127.0.0.1:8000/api/image/images` endpoint, login with created credentials and now we can upload image as well as get paginated list of links to our images.
