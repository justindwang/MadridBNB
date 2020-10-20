import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { HttpClientModule } from '@angular/common/http';

import { RouterModule, Routes} from '@angular/router';
import { AppComponent } from './app.component';
import { ListingsComponent } from './listings/listings.component';

const routes: Routes = [
  {path: '', component: ListingsComponent},
];

@NgModule({
  declarations: [
    AppComponent,
    ListingsComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    RouterModule.forRoot(routes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
