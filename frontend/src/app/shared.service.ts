import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
  readonly APIUrl = 'http://localhost:8105';

  constructor(private http:HttpClient) { }

  getCompaniesList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/companies/');
  }
}
