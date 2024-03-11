async function getGithubData() {
    url ='"{{ link }}"'
let response = await fetch(url)
let data = await response.json()
console.log(data)
}
getGithubData()