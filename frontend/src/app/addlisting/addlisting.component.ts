import { Component, OnInit } from '@angular/core';
import { ApiCallService } from '../api-call.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-listings',
  templateUrl: './addlisting.component.html',
  styleUrls: ['./addlisting.component.css'],
})

export class AddlistingComponent implements OnInit {
  listingData;
  

  constructor(
    private API : ApiCallService, //service that calls our API
    private router : Router
  ) 
  {
    this.listingData = 
      {
        id: null, //this will not be set
        neighborhood: null,
        roomType: null,
        pricing: null
      };

  }

  ngOnInit() {
    
  }

  setNeighborhood(neighborhood){
    this.listingData.neighborhood = neighborhood;
    //console.log('SET NEIGHBORHOOD:' + neighborhood);
  }

  setRoomType(roomType){
    this.listingData.roomType = roomType;
    //console.log('SET ROOM TYPE:' + roomType);
  }

  addPricing(pricing){
    this.listingData.pricing = parseInt(pricing);
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
          } else { //invalid response
            console.log("Invalid Response");
            this.router.navigateByUrl('listings');
          }
        }
      );
  }

}

