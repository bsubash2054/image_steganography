provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_namespace" "steganography-namespace" {
  metadata {
    name = "steganography"
  }
}

resource "kubernetes_deployment" "steganography-deployment" {
  metadata {
    name      = "steganography-deployment"
    namespace = kubernetes_namespace.steganography-namespace.metadata[0].name
    labels = {
      app = "steganography"  # Label for the deployment
    }
  }

  spec {
    replicas = 2

    selector {
      match_labels = {
        app = "steganography"  # Matching label for the pods
      }
    }

    template {
      metadata {
        labels = {
          app = "steganography"  # Label for the pods
        }
      }

      spec {
        container {
          image = "544234170512.dkr.ecr.us-east-1.amazonaws.com/stenography:7f314b9"
          name  = "steganography-container"

          # If you need to specify environment variables or ports, you can do it here
          # env {
          #   name  = "ENV_VARIABLE_NAME"
          #   value = "ENV_VARIABLE_VALUE"
          # }
        }
      }
    }
  }
}

resource "kubernetes_service" "steganography-service" {
  metadata {
    name      = "steganography-service"
    namespace = kubernetes_namespace.steganography-namespace.metadata[0].name
  }

  spec {
    type = "LoadBalancer"

    selector = {
      app = kubernetes_deployment.steganography-deployment.spec[0].template[0].metadata[0].labels["app"]
    }

    port {
      port        = 80
      target_port = 8000
    }
  }
}