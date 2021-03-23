<template>
  <div class="jumbotron search_component">
    <h1 class="header_title display-4">Search Bhav Copy</h1>
    <hr class="my-4" />
    <form @submit="checkForm" action="">
      <div class="form-group">
        <div class="search_input">
          <input
            type="text"
            v-model="name"
            class="form-control"
            id="searchInputKeyword"
            aria-describedby="searchHelp"
            required="true"
            placeholder="Enter name of the company"
          />
        </div>
        <div class="search_action">
          <button
            type="submit"
            class="search_btn btn btn-primary"
            @click="search"
          >
            <span v-if="!searching">
              Search
            </span>
            <b-icon
              v-if="searching"
              icon="three-dots"
              animation="cylon"
            ></b-icon>
          </button>
        </div>
      </div>
    </form>
    <hr class="my-4" v-if="results && results.length > 0" />
    <table class="results_table table table-striped" v-if="results && results.length > 0">
      <thead>
        <tr>
          <th scope="col">
            <a role="button" data-mdb-toggle="tooltip" title="Row Number">#</a>
          </th>
          <th scope="col" class="sc_name">
            <a
              role="button"
              data-mdb-toggle="tooltip"
              title="Name of the company"
              >Name</a
            >
          </th>
          <!-- <th scope="col">
            <a
              role="button"
              data-mdb-toggle="tooltip"
              title="Unique code assigned to a scrip of a company by BSE"
              >Code</a
            >
          </th> -->
          <th scope="col">
            <a
              role="button"
              data-mdb-toggle="tooltip"
              title="The price at which the security first trades on a given trading day"
              >Open</a
            >
          </th>
          <th scope="col">
            <a
              role="button"
              data-mdb-toggle="tooltip"
              title="The highest intra-day price of a stock"
              >High</a
            >
          </th>
          <th scope="col">
            <a
              role="button"
              data-mdb-toggle="tooltip"
              title="The lowest intra-day price of a stock."
              >Low</a
            >
          </th>
          <th scope="col">
            <a
              role="button"
              data-mdb-toggle="tooltip"
              title="The final price at which a security is traded on a given trading day"
              >Close</a
            >
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(result,index) in results" :key="result.keyname">
          <th scope="row">{{++index}}</th>
          <td class="sc_name">{{result.keyname}}</td>
          <td>{{result.open}}</td>
          <td>{{result.high}}</td>
          <td>{{result.low}}</td>
          <td>{{result.close}}</td>
        </tr>
      </tbody>
    </table>
    <div v-if="notFound" class="notFound">
      keyword does not match any name
    </div>
    <hr class="my-4" />
    <div></div>

  </div>
  
</template>

<script>
import axios from 'axios';
export default {
  name: 'Search',
  data() {
    return {
      name: null,
      searching: false,
      results: [],
      notFound: false
    };
  },
  methods: {
    checkForm(e) {
      e.preventDefault();
    },
    search() {
      const apiUrl = "http://165.22.214.254:8000/api/search?value="
      console.log('search');
      if (this.name && this.name.length) {
        console.log(this.name);
        const finalUrl = apiUrl + this.name;
        this.searching = true;
        this.results = [];
        axios
          .get(finalUrl)
          .then(
            (response) => {
            this.searching = false;
            this.notFound = false;
            console.log(response["data"]["SearchResults"]);
            this.results = response["data"]["SearchResults"]
          }, err =>{
            this.notFound = true;
            this.searching = false;
            console.log(err);
          });
      } else {
        console.log('Enter name');
      }
    },
  },
};
</script>

<style>
.header_title {
  text-align: left;
  font-size: 40px;
  font-family:fantasy
}
table {
  background: #fff;
}
table tbody {
  display: block;
  max-height: 294px;
  overflow-y: auto;
}

table thead,
table tbody tr {
  display: table;
  width: 100%;
  table-layout: fixed;
}

table td {
  vertical-align: middle !important;
}

table th {
  vertical-align: middle !important;
}
.sc_name {
  text-align: left;
  max-width: 250px;
  overflow-wrap: break-word;
}
.search_input input {
  height: 50px;
  font-size: 20px;
  font-weight: 600;
  font-family:fantasy
}
#searchInputKeyword::placeholder {
  font-size: 20px;
  font-weight: 400;
}
.search_input small {
  text-align: left;
  margin-left: 3px;
  
}
.search_action {
  margin-top: 15px;
}
.search_action button {
  width: 290px;
  height: 50px;
  font-size: 20px;
  font-weight: 600;
}
.search_component {
  margin: 0 auto;
  max-width: 1024px;
}
.results_table {
  margin-top: 30px;
}
.notFound {
  font-size: 15px;
  font-weight: 600;
  font-family: arial;
}
</style>
