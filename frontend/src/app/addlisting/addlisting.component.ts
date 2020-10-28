import { Component, OnInit } from '@angular/core';
import { ApiCallService } from '../api-call.service';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-listings',
  templateUrl: './addlisting.component.html',
  styleUrls: ['./addlisting.component.css'],
})

export class AddlistingComponent implements OnInit {
  enterData; 
  searchData;//search data
  listings;
  

  constructor(
    private API : ApiCallService, //service that calls our API
    private formBuilder : FormBuilder
  ) 
  {
    this.enterData = 
      {
        id: null, //this will never be set
        neighborhood: null,
        roomType: null,
        floorprice: null,
        ceilprice: null
      };

  }

  ngOnInit() {
    
  }

  addNeighborhood(neighborhood){
    this.enterData.neighborhood = neighborhood;
    //console.log('SET NEIGHBORHOOD:' + neighborhood);
  }

  setRoomType(roomType){
    this.enterData.roomType = roomType;
    //console.log('SET ROOM TYPE:' + roomType);
  }

  addPricing(pricing){
    this.enterData.pricing = parseInt(pricing);
    //console.log('SET FLOOR PRICE:' + floorprice);
  }



  //sends a post request to the server
  makeSearch(searchData){
    console.log("Sending request");
    console.log(searchData);

    //reset searchForm
    this.searchData = 
      {
        id: null, //this will never be set
        neighborhood: null,
        roomType: null,
        floorprice: null,
        ceilprice: null
      };
    let response = undefined; //this should be a list of listings objects
    this.API.getListings(searchData) //make the API call
      .subscribe( //this runs when the post request gets a response
        (result) => {
          response = result;
        }
      ).add( //this runs after the post reponse has been recieved
        () => {
          if (response != undefined){ //valid response
            this.listings = response.listings; //reponse should be a list of listings objects
          } else { //invalid response

          }
        }
      );
  }

}

