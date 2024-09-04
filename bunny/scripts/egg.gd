extends StaticBody2D

#@export var chicken_scene: PackedScene # Escena del pollo que se creará
@export var chicken_spawn_position: Vector2 # Posición donde aparecerá el nuevo pollo
var chicken_scene
@onready var timer: Timer = null

func _ready():
	chicken_scene = preload("res://scenes/chicken.tscn")
	timer = $Timer
	if timer == null:
		# Si no se encuentra el Timer, se crea programáticamente
		timer = Timer.new()
		add_child(timer)
	timer.wait_time = 2.0 # 3 segundos
	timer.one_shot = true # Solo se ejecuta una vez
	timer.start()

	# Conectar la señal timeout del Timer al método _on_timer_timeout
	timer.connect("timeout", _on_timer_timeout)

func _on_area_2d_area_entered(area):
	if area.name == "Chicken": # Verifica que sea un pollo el que entró en el área
		remove_from_group("eggs")
		queue_free()
		_spawn_new_chicken()

func _on_timer_timeout() -> void:
	queue_free() # Elimina el huevo si han pasado 3 segundos

func _spawn_new_chicken() -> void:
	# Instancia un nuevo pollo
	var new_chicken = chicken_scene.instantiate() #as Node2D

	# Establece la posición inicial del nuevo pollo
	new_chicken.position = self.position

	# Añade el nuevo pollo al árbol de nodos
	get_tree().current_scene.add_child(new_chicken)
