package com.ashish.gotal.users.controller;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

@Path("/users")
public class UserController {

  @GET
  @Produces(MediaType.APPLICATION_JSON)
  public String sayPlainTextHello() {
    return "Get Users";
  }
}
