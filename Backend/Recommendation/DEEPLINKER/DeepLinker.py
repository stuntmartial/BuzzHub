import tensorflow as tf
from tensorflow import keras
from spektral.layers import GATConv as GAT

class DEEPLINKER(keras.models.Model):

    """
        DEEPLINKER Model uses two GATs to generate enriched node feature
        representations , computes Hadamard Distance between the node
        pairs , and finally pass it through a Logistic Regression Layer to 
        compute the link-existance probablity 
    """

    def __init__(self,intermediate_dims=150,out_dims=100):
        super(DEEPLINKER,self).__init__()
        
        self.intermediate_dims=intermediate_dims
        self.out_dims=out_dims
        self.attn_heads1=8
        self.attn_heads2=1
        
        self.GAT1=GAT(  channels=self.intermediate_dims,
                        attn_heads=self.attn_heads1,
                        concat_heads=False,
                        dropout_rate=0.6,
                        activation=tf.nn.elu
                    )

        self.GAT2=GAT(  channels=self.out_dims,
                        attn_heads=1,
                        activation=tf.nn.elu
                    )
    
    def build(self,input_shape):

        self.W=self.add_weight( shape=(348,348),
                                initializer=keras.initializers.glorot_uniform,
                                trainable=True,
                                name='weight'
                            )

        self.bias=self.add_weight(  shape=(348,348),
                                    initializer=keras.initializers.constant(value=-1),
                                    trainable=True,
                                    name='bias'
                                )

    def call(self,inputs):
        
        node_feats=inputs[0]
        adj_matrix=inputs[1]
        node_embs_GAT1=self.GAT1([node_feats,adj_matrix])
        node_embs_GAT2=self.GAT2([node_embs_GAT1,adj_matrix])
        op=tf.matmul(node_embs_GAT2,tf.transpose(node_embs_GAT2))
        op=tf.matmul(self.W,op)
        op=tf.math.add(op,self.bias)
        op=tf.nn.sigmoid(op)
        return op
