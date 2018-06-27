function Passenger() {
            this.currentTrip = null;
            this.upcomingTrips = [];
            this.pastTrips = [];
        }
        function User(name, PID, email, username, password, driver, passenger, userType) {
            this.name = name;
            this.phonenumber = phonenumber;
            this.email = email;
            this.username = username;
            this.password = password;
            this.driver = driver;
            this.passenger = passenger;
            this.userType = userType;
        }
        function next() {
            var name = document.getElementById("name").value;
            var phonenumber = document.getElementById("phonenumber").value;
            var email = document.getElementById("email").value;
            var username = document.getElementById("username").value;
            var password = document.getElementById("password").value;

            if ( !(name && phonenumber && email && username && password) ) {
                alert("Please enter all the required fields");
                return;
            }
    
            var passenger = new Passenger();
            var user = new User(name, phonenumber, email, username, password, null, passenger, "passenger");

            if ( localStorage.getItem(username) ) {
                alert("Username is used. Please change one.");
            }
            else {
                localStorage.setItem(username, JSON.stringify(user));
                sessionStorage.setItem("userType", "passenger");
                window.location.href = "Login.html";
            }

            var retrieved = localStorage.getItem("passengerArray");
            if (retrieved == null) {
                var passengerArray = [];
                passengerArray.push(username);
                localStorage.setItem("passengerArray", JSON.stringify(passengerArray));
            }
            else {
                var passengerArray = JSON.parse(retrieved);
                passengerArray.push(username);
                localStorage.setItem("passengerArray", JSON.stringify(passengerArray));
            }
        }