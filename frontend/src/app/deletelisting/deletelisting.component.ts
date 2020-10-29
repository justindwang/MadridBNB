import { Component, OnInit } from '@angular/core';
import { ApiCallService } from '../api-call.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-deletelisting',
  templateUrl: './deletelisting.component.html',
  styleUrls: ['./deletelisting.component.css']
})
export class DeletelistingComponent implements OnInit {

  listingData;

  constructor(
    private API : ApiCallService, //service that calls our API
    private router : Router
  ) 
  {
    this.listingData = 
      {
        id: null, 
        neighborhood: null,
        roomType: null,
        pricing: null
      };

  }

  ngOnInit() {
    
  }

  setlistingID(id){
    this.listingData.id = parseInt(id);
  }

  //sends a post request to the server
  makeEnter(listingData){
    console.log("Sending request");
    console.log(listingData);

    let response = undefined; //this should be a list of listings objects
    this.API.removeListing(listingData) //make the API call
      .subscribe( //this runs when the post request gets a response
        (result) => {
          response = result;
        }
      ).add( //this runs after the post reponse has been recieved
        () => {
          if (response != undefined){ //valid response
            console.log("Valid Reponse");
            this.router.navigateByUrl('listings');
          } else { //invalid response
            console.log("Invalid Response");
            this.router.navigateByUrl('listings');
          }
        }
      );
  }
  

}
