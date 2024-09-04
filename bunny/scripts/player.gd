extends CharacterBody2D

@onready var anim_tree = $AnimationTree
@onready var state_machine = $AnimationTree.get("parameters/playback")
#@onready var egg = $StaticBody2D

var input_vector
var egg

func _ready():
	egg = preload("res://scenes/egg.tscn")

func set_blend_position(vector):
	anim_tree.set("parameters/Idle/blend_position", vector)
	anim_tree.set("parameters/Run/blend_position", vector)
	anim_tree.set("parameters/Axe/blend_position", vector)
	anim_tree.set("parameters/Pick/blend_position", vector)

func _on_player_control_do_move(incoming_input_vector: Vector2) -> void:
	input_vector = incoming_input_vector
	set_blend_position(input_vector)
	state_machine.travel("Run")


func _on_player_control_do_attack() -> void:
	print(input_vector)
	set_blend_position(input_vector)
	state_machine.travel("Axe")
	
func _process(delta: float):
	if Input.is_action_just_pressed("drop_egg"):
		_drop_egg()

func _drop_egg() -> void:
	# Instancia una nueva escena Egg
	var new_egg = egg.instantiate() #as Marker2D
	
	# Establece la posición del nuevo huevo (puedes ajustar esto según tus necesidades)
	new_egg.position = self.position
	
	new_egg.add_to_group("eggs")
	# Añade el huevo como hijo al árbol de nodos (por ejemplo, a la raíz de la escena actual)
	get_tree().current_scene.add_child(new_egg)
	
