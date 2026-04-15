use actix_web::{get, web, App, HttpRequest, HttpServer, Responder};
use chrono::Local; // <-- cambiamos a Local
use serde::Serialize;

#[derive(Serialize)]
struct InfoResponse {
    user_agent: String,
    time: String,
    name: String,
}

#[get("/")]
async fn root(req: HttpRequest, query: web::Query<std::collections::HashMap<String, String>>) -> impl Responder {
    // Obtener el parámetro "name" de la query string
    let nombre = query.get("name").cloned().unwrap_or("Miguel".to_string());

    // Obtener el user-agent
    let user_agent = req
        .headers()
        .get("User-Agent")
        .and_then(|ua| ua.to_str().ok())
        .unwrap_or("Desconocido")
        .to_string();

    // Hora actual en formato ISO pero usando la zona horaria local
    let hora_servicio = Local::now().to_rfc3339();

    // Respuesta JSON
    web::Json(InfoResponse {
        name: nombre,
        user_agent,
        time: hora_servicio,
    })
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .service(root) // Registrar el endpoint en "/"
    })
    .bind(("127.0.0.1", 3000))?
    .run()
    .await
}
