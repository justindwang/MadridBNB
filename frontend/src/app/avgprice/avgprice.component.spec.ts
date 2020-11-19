import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AvgpriceComponent } from './avgprice.component';

describe('AvgpriceComponent', () => {
  let component: AvgpriceComponent;
  let fixture: ComponentFixture<AvgpriceComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AvgpriceComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AvgpriceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
