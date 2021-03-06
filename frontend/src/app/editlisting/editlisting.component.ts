import { Component, OnInit } from '@angular/core';
import { ApiCallService } from '../api-call.service';
import  {Router } from '@angular/router';

@Component({
  selector: 'app-editlisting',
  templateUrl: './editlisting.component.html',
  styleUrls: ['./editlisting.component.css']
})
export class EditlistingComponent implements OnInit {

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
        price: null
      };

  }

  ngOnInit() {
    
  }

  setListingID(id){
    this.listingData.id = parseInt(id);
  }

  setNeighborhood(neighborhood){
    this.listingData.neighborhood = neighborhood;
    //console.log('SET NEIGHBORHOOD:' + neighborhood);
  }

  setRoomType(roomType){
    this.listingData.roomType = roomType;
    //console.log('SET ROOM TYPE:' + roomType);
  }

  setPricing(pricing){
    this.listingData.price = parseInt(pricing);
  }


  //sends a post request to the server
  makeEnter(listingData){
    console.log("Sending request");
    console.log(listingData);

    let response = undefined; //this should be a list of listings objects
    this.API.editListing(listingData) //make the API call
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
