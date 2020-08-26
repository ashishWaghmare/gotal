package com.ashish.gotal.controller;

import io.micronaut.http.MediaType;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.annotation.Produces;


@Controller("/inventory")
public class InventoryController {

  @Get
  @Produces(MediaType.TEXT_PLAIN)
  public String index() {
    return "Hello Inventory";
  }
}
