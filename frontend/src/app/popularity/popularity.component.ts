import { Component, OnInit } from '@angular/core';
import { ApiCallService } from '../api-call.service';

@Component({
  selector: 'app-popularity',
  templateUrl: './popularity.component.html',
  styleUrls: ['./popularity.component.css']
})

export class PopularityComponent implements OnInit {
  popular_madrid;
  popular_neighborhoods;
  neighborhood_pop:boolean = true;
  madrid_pop:boolean = true;

  constructor(
    private API : ApiCallService, //service that calls our API
  )
  {

  }

  ngOnInit() {
    this.makeEnter();
  }

  madridpop_display(){
    this.madrid_pop= !this.madrid_pop;
   
  }

  neighborhoodpop_display(){
    this.neighborhood_pop = !this.neighborhood_pop;
  }


  
  //sends a get request to the server
  makeEnter(){
    console.log("Sending request");
    console.log();

    let response = undefined; //this should be a list of listings objects
    this.API.getAnalytics() //make the API call
      .subscribe( //this runs when the get request gets a response
        (result) => {
          response = result;
        }
      ).add( //this runs after the post reponse has been recieved
        () => {
          if (response != undefined){ //valid response
            this.popular_madrid = response.top_listings;
            this.popular_neighborhoods = response.top_neighborhoods;

            console.log("Valid Reponse");
            console.log(response);
          } else { //invalid response
            console.log("Invalid Response");
          }
        }
      );
  }
}
