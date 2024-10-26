# Django Bus Example

## To Setup
Clone Repo

```
pip install -r requirements.txt in root
cd app
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Demo Time!
- Add an agency from the left nav bar
- Add a bus
- On the bus detail page, add a departure time.  Note: Bus detail page will show the seat diagram
- After adding a trip, view the trip
- Go into the admin, and assign your user to one of the SeatUserLink slots
- Refresh trip page to see that it shows your seat is taken
