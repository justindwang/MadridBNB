import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-popularity',
  templateUrl: './popularity.component.html',
  styleUrls: ['./popularity.component.css']
})
export class PopularityComponent implements OnInit {

  constructor() { 

    private API : ApiCallService, //service that calls our API
    private router : Router
  }

  ngOnInit() {
  }

  
  //sends a post request to the server
  makeEnter(listingData){
    console.log("Sending request");
    console.log(listingData);

    let response = undefined; //this should be a list of listings objects
    this.API.addListing(listingData) //make the API call
      .subscribe( //this runs when the post request gets a response
        (result) => {
          response = result;
        }
      ).add( //this runs after the post reponse has been recieved
        () => {
          if (response != undefined){ //valid response
            console.log("Valid Reponse");
            this.router.navigateByUrl('listings');
            console.log(response);
          } else { //invalid response
            console.log("Invalid Response");
            this.router.navigateByUrl('listings');
          }
        }
      );
  }

}
