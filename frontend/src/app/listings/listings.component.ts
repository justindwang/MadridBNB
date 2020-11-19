import { Component, OnInit } from '@angular/core';
import { ApiCallService } from '../api-call.service';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-listings',
  templateUrl: './listings.component.html',
  styleUrls: ['./listings.component.css'],
})

export class ListingsComponent implements OnInit {
  searchForm; //search data
  listings; //list of all recieved listings. contains listings objects

  average_price;
  cheap_listings;
  expensive_listings;
  ShowMe:boolean = false;

  cheap = false;
  expensive = true;

  constructor(
    private API : ApiCallService, //service that calls our API
    private formBuilder : FormBuilder
  ) 
  {
    this.searchForm = 
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

  setNeighborhood(neighborhood){
    this.searchForm.neighborhood = neighborhood;
    //console.log('SET NEIGHBORHOOD:' + neighborhood);
  }

  setRoomType(roomType){
    this.searchForm.roomType = roomType;
    //console.log('SET ROOM TYPE:' + roomType);
  }

  setFloorPrice(floorprice){
    this.searchForm.floorprice = parseInt(floorprice);
    //console.log('SET FLOOR PRICE:' + floorprice);
  }

  setCeilPrice(ceilprice){
    this.searchForm.ceilprice = parseInt(ceilprice);
    //console.log('SET CEIL PRICE:' + ceilprice);
  }

  toggle_display(string){
    if (string == 'cheap'){
      this.cheap = true;
      this.expensive = false;
    } else if (string == 'expensive'){
      this.expensive = true;
      this.cheap = false;
    }
  }

  


  //sends a post request to the server
  makeSearch(searchData){
    console.log("Sending request");
    console.log(searchData);

    this.ShowMe = true;

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
            this.cheap_listings = response.cheap_listings;
            this.expensive_listings = response.expensive_listings;
            this.average_price = response.average_price;

            console.log("Valid Response");
            console.log(response);
          } else { //invalid response
            console.log("Invalid Response");
          }
        }
      );
  }

}
