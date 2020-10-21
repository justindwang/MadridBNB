import { Component, OnInit } from '@angular/core';
import { ApiCallService } from '../api-call.service';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-listings',
  templateUrl: './listings.component.html',
  styleUrls: ['./listings.component.css']
})
export class ListingsComponent implements OnInit {
  searchForm; //search data
  listings; //list of all recieved listings. contains listings objects

  constructor(
    private API : ApiCallService, //service that calls our API
    private formBuilder : FormBuilder
  ) 
  {
    this.searchForm = this.formBuilder.group( //this is the searchData that will be sent via post request
      {
        id: null, //this will never be set
        neighborhood: null,
        roomType: null,
        priceRange: null
      }
    );

  }

  ngOnInit() {
  }

  //sends a post request to the server
  makeSearch(searchData){
    let response = undefined; //this should be a list of listings objects
    this.API.getListings(searchData) //make the API call
      .subscribe( //this runs when the post request gets a response
        (result) => {
          response = result;
        }
      ).add( //this runs after the post reponse has been recieved
        () => {
          if (response != undefined){ //valid response
            this.listings = response; //reponse should be a list of listings objects
          } else { //invalid response

          }
        }
      );
  }

}
