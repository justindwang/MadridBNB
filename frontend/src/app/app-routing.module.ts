import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ListingsComponent } from './listings/listings.component'
import { AddlistingComponent } from './addlisting/addlisting.component'
import { EditlistingComponent } from './editlisting/editlisting.component'
const routes: Routes = [

    {path: 'listings', component: ListingsComponent},
    {path: 'addlisting', component: AddlistingComponent},
    {path: 'editlisting', component: EditlistingComponent}
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})

export class AppRoutingModule {}
export const routingComponents = [ListingsComponent, AddlistingComponent,EditlistingComponent]