import { Component, OnInit } from '@angular/core';
import { ApiCallService } from '../api-call.service';
import  {Router } from '@angular/router';

@Component({
  selector: 'app-editlisting',
  templateUrl: './reviews.component.html',
  styleUrls: ['./reviews.component.css']
})
export class ReviewsComponent implements OnInit {

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

  setReview(review){
    this.listingData.review = review;
    //console.log('SET NEIGHBORHOOD:' + neighborhood);
  }

  //sends a post request to the server
  makeEnter(listingData){
    console.log("Sending request");
    console.log(listingData);

    let response = undefined; //this should be a list of listings objects
    this.API.addReviews(listingData) //make the API call
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
