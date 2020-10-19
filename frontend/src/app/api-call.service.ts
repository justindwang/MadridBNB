import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiCallService {

  constructor(
    private http: HttpClient
  ) { }

  getListings(searchData){
    //returns listing data based on inputted searchData
    /*searchData = {
      "neighborhood" : None,
      "roomType" : None,
      "priceRange" : [0,100]
    }
    */
    return this.http.post<any>('http://127.0.0.1:5000/listings', searchData);
  }

  getReviews(searchData){
    //returns review data based on inputted searchData
    /*searchData = {
      "dateRange" : [],
      "reviewerName" : "Name"
    */
    return this.http.post<any>('http://127.0.0.1:5000/reviews', searchData);
  }

  getNeighborhoods(searchData){
     //returns neighborhood data based on inputted searchData
    /*searchData = {
      "neighborhoodName" : "Name",
      "neighboorhoodGroup" : "Name"
    */
    return this.http.post<any>('http://127.0.0.1:5000/reviews', searchData);
  }
}
