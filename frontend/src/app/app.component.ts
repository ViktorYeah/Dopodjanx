import { Component } from '@angular/core';
import { SharedService } from './shared.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(private service:SharedService){
  }

  public companies:any = [];
  
  ngOnInit(): void{
    this.refreshCompaniesList();
  }

  refreshCompaniesList() {
    this.service.getCompaniesList().subscribe(res => {
      this.companies = res;
    })

    console.log('companies' + this.companies);
  }
}
